---
{
  "projection_kind": "taulib_declaration",
  "title": "axiom_min_depth",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/axiom-min-depth/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::axiom_min_depth",
  "declaration_slug": "axiom-min-depth",
  "kind": "def",
  "name": "axiom_min_depth",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 62,
  "source_line_end": 71,
  "registry_ids": [
    "III.D68"
  ],
  "related_registry_items": [
    {
      "id": "III.D68",
      "title": "Gödel Numbering as NF Address",
      "url": "/registry/object/III.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L62-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L62-L71",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L62-L71)
- Source range: L62-L71
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D68` — Gödel Numbering as NF Address

## Immediate Comment / Docstring

```lean
/-- [III.D68] Each axiom has a primorial depth requirement: the minimum
    depth k at which the axiom's operation is expressible. -/
```

## Source Excerpt

```lean
def axiom_min_depth : ZFCAxiom -> Nat
  | .extensionality => 1   -- equality at any level >= 1
  | .pairing        => 1   -- pair {a,b} = (a + b * p) mod P_k
  | .union          => 2   -- union needs two-prime decomposition
  | .powerset       => 2   -- powerset needs exponential capacity
  | .infinity       => 3   -- infinity needs unbounded tower
  | .separation     => 1   -- filter by predicate at any level
  | .replacement    => 2   -- image needs composition of two stages
  | .foundation     => 1   -- well-foundedness at any level
  | .choice         => 2   -- choice function needs at least 2 primes
```
