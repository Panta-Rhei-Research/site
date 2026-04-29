---
{
  "projection_kind": "taulib_declaration",
  "title": "limit_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-local-fields/limit-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.LocalFields`.",
  "declaration_id": "TauLib.BookIII.Spectral.LocalFields::limit_uniqueness_check",
  "declaration_slug": "limit-uniqueness-check",
  "kind": "def",
  "name": "limit_uniqueness_check",
  "module_name": "TauLib.BookIII.Spectral.LocalFields",
  "module_url": "/verify/taulib/docs/book-iii-spectral-local-fields/",
  "source_line_start": 143,
  "source_line_end": 168,
  "registry_ids": [
    "III.P06"
  ],
  "related_registry_items": [
    {
      "id": "III.P06",
      "title": "Completeness Without Topology",
      "url": "/registry/object/III.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L143-L168",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.LocalFields",
        "url": "/verify/taulib/docs/book-iii-spectral-local-fields/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L143-L168",
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

- Module: [TauLib.BookIII.Spectral.LocalFields](/verify/taulib/docs/book-iii-spectral-local-fields/)
- Source path: [`TauLib/BookIII/Spectral/LocalFields.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/LocalFields.lean#L143-L168)
- Source range: L143-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P06` — Completeness Without Topology

## Immediate Comment / Docstring

```lean
/-- [III.P06] Uniqueness of limit: two tower-coherent sequences that
    agree at all levels are equal (= same element of ℤ_p^τ). -/
```

## Source Excerpt

```lean
def limit_uniqueness_check (bound depth : TauIdx) : Bool :=
  go 0 0 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 (fuel - 1)
    else
      let p : Nat := 3  -- test prime
      -- If x ≡ y mod p^d for all d ≤ depth, then x = y mod p^depth
      let agree_all := check_agreement x y p 1 (depth + 1)
      let conclusion := if agree_all then
        let pd := p ^ depth
        if pd > 0 then x % pd == y % pd else true
      else true
      conclusion && go x (y + 1) (fuel - 1)
  termination_by fuel
  check_agreement (x y p d fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if d > depth then true
    else
      let pd := p ^ d
      if pd > 0 then
        x % pd == y % pd && check_agreement x y p (d + 1) (fuel - 1)
      else true
  termination_by fuel
```
