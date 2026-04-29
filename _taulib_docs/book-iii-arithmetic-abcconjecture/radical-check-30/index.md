---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_check_30",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/radical-check-30/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::radical_check_30",
  "declaration_slug": "radical-check-30",
  "kind": "theorem",
  "name": "radical_check_30",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 189,
  "source_line_end": 190,
  "registry_ids": [
    "III.D97"
  ],
  "related_registry_items": [
    {
      "id": "III.D97",
      "title": "Radical Function",
      "url": "/registry/object/III.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L189-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCConjecture",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L189-L190",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIII.Arithmetic.ABCConjecture](/verify/taulib/docs/book-iii-arithmetic-abcconjecture/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L189-L190)
- Source range: L189-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D97` — Radical Function

## Immediate Comment / Docstring

```lean
/-- [III.D97] Radical is well-defined and idempotent up to 30. -/
```

## Source Excerpt

```lean
theorem radical_check_30 :
    radical_check 30 = true := by native_decide
```
