---
{
  "projection_kind": "taulib_declaration",
  "title": "self_apply",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/self-apply/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::self_apply",
  "declaration_slug": "self-apply",
  "kind": "def",
  "name": "self_apply",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 53,
  "source_line_end": 56,
  "registry_ids": [
    "III.D83"
  ],
  "related_registry_items": [
    {
      "id": "III.D83",
      "title": "Kleene Fixed Point",
      "url": "/registry/object/III.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L53-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L53-L56",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L53-L56)
- Source range: L53-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D83` — Kleene Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D83] Self-application operator S(c) = (c + c) mod M_k.
    Models code applied to itself (Kleene's recursion theorem). -/
```

## Source Excerpt

```lean
def self_apply (c k : Nat) : Nat :=
  let pk := primorial k
  if pk == 0 then 0
  else (c + c) % pk
```
