
#include "zerynth.h"

C_NATIVE(_totuple) {
    NATIVE_UNWARN();

    CHECK_ARG(args[0], PLIST);
    uint32_t list_len = PSEQUENCE_ELEMENTS(args[0]);
    PTuple *mtuple = (PTuple *) psequence_new(PTUPLE, list_len);

    for (uint32_t i=0; i<list_len; i++) {
        PTUPLE_SET_ITEM(mtuple, i, PLIST_ITEM(args[0], i));
    }

    *res = mtuple;
    return ERR_OK;  
}
