#include <Python.h>
#include "graph7/src/graph7.h"

static void raise_err(int32_t err)
{
    if(err == 0)
        return;

    switch(abs(err))
    {
    case GRAPH7_INVALID_ARG:
        PyErr_SetString(PyExc_ValueError, "The invalid argument");
        break;
    case GRAPH7_INVALID_LENGTH:
        PyErr_SetString(PyExc_ValueError, "Error during decoding. The invalid graph7 string");
        break;
    case GRAPH7_INVALID_HEADER:
        PyErr_SetString(PyExc_ValueError, "Error during decoding. The invalid graph7 string");
        break;
    case GRAPH7_INVALID_DATA:
        PyErr_SetString(PyExc_ValueError, "Error during decoding. The invalid graph7 string");
        break;
    case GRAPH7_ALLOC_ERROR:
        PyErr_SetString(PyExc_MemoryError, "Not enough memory");
        break;
    default:
        PyErr_SetString(PyExc_RuntimeError, "Unknown error");
    }
}

static PyObject* encode(PyObject *self, PyObject *args)
{
    const char *src;
    int32_t length;
    uint32_t order;
    int32_t gtype;
    uint32_t width;

    PyObject *retval = NULL;

    uint8_t *dst;

    int32_t err = 0;

    if(!PyArg_ParseTuple(args, "y#IiI", &src, &length, &order, &gtype, &width))
        goto _exit;

    if(length/(width ? width : 1) != order * order || order < 2)
    {
        err = GRAPH7_INVALID_ARG;
        goto _exit;
    }

    dst = (uint8_t *)malloc(graph7_encoding_length(order * order, width));

    if(!dst)
    {
        err = GRAPH7_ALLOC_ERROR;
        goto _exit;
    }

    length = graph7_encode_from_matrix(dst, (const uint8_t *)src, order, gtype, width);

    if(length < 0)
    {
        err = length;
        goto _exit;
    }

    retval = PyBytes_FromStringAndSize((const char *)dst, (Py_ssize_t)length);

_exit:
    if(dst)
        free(dst);

    raise_err(err);

    return retval;
}

static PyObject* decode(PyObject *self, PyObject *args)
{
    const char *src;
    int32_t length;

    PyObject *retval = NULL;

    int32_t gtype;
    uint32_t width;

    int32_t decoding_length;

    int32_t order;
    uint8_t *dst;

    int32_t err = 0;

    if(!PyArg_ParseTuple(args, "y#", &src, &length))
        goto _exit;

    decoding_length = graph7_metadata(src, length, &gtype, &width);

    if(decoding_length < 0)
    {
        err = decoding_length;
        goto _exit;
    }

    order = graph7_order(decoding_length / width, gtype);
    dst = (uint8_t *)malloc(order * order * width);

    if(!dst)
    {
        err = GRAPH7_ALLOC_ERROR;
        goto _exit;
    }

    if((decoding_length = graph7_decode_to_matrix(dst, src, length)) < 0)
    {
        err = decoding_length;
        goto _exit;
    }

    retval = Py_BuildValue("(y#l)", (const char *)dst, order * order * width, width);

_exit:
    if(dst)
        free(dst);

    raise_err(err);

    return retval;
}

static PyMethodDef methods[] =
{
    {"encode", encode, METH_VARARGS, ""},
    {"decode", decode, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef definition =
{
    PyModuleDef_HEAD_INIT,
    "_graph7",
    "",
    -1,
    methods
};

PyMODINIT_FUNC PyInit__graph7(void)
{
    Py_Initialize();
    return PyModule_Create(&definition);
}
