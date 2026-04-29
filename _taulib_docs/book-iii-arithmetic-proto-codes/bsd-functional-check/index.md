---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_functional_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/bsd-functional-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::bsd_functional_check",
  "declaration_slug": "bsd-functional-check",
  "kind": "def",
  "name": "bsd_functional_check",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 107,
  "source_line_end": 119,
  "registry_ids": [
    "III.D62"
  ],
  "related_registry_items": [
    {
      "id": "III.D62",
      "title": "BSD Functional",
      "url": "/registry/object/III.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L107-L119",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L107-L119",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L107-L119)
- Source range: L107-L119
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D62` — BSD Functional

## Immediate Comment / Docstring

```lean
/-- [III.D62] BSD functional check: the functional is well-defined and
    non-negative at each level. -/
```

## Source Excerpt

```lean
def bsd_functional_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let bsd := bsd_functional k
      let pk := primorial k
      -- BSD positive when computable and both sectors present
      let ok := if k >= 3 && pk > 0 && pk <= 100 then bsd > 0 else true
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
