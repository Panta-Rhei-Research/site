---
{
  "projection_kind": "taulib_declaration",
  "title": "arith_translation_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/arith-translation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::arith_translation_check",
  "declaration_slug": "arith-translation-check",
  "kind": "def",
  "name": "arith_translation_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 59,
  "source_line_end": 76,
  "registry_ids": [
    "III.D87"
  ],
  "related_registry_items": [
    {
      "id": "III.D87",
      "title": "Arithmetic Translation Functor",
      "url": "/registry/object/III.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L59-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L59-L76",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L59-L76)
- Source range: L59-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D87` — Arithmetic Translation Functor

## Immediate Comment / Docstring

```lean
/-- [III.D87] Arithmetic translation check: verify the embedding is
    well-defined and injective at each stage. -/
```

## Source Excerpt

```lean
def arith_translation_check (bound db : Nat) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let xr := x % pk
        -- Well-defined: arith_translate gives a value in [0, M_k)
        let wd := arith_translate xr k < pk
        -- Reduce-stable: arith_translate of a reduced value is itself
        let stable := arith_translate xr k == xr
        wd && stable && go x (k + 1) (fuel - 1)
  termination_by fuel
```
