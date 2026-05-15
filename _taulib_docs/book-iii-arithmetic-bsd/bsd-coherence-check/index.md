---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_coherence_check",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-bsd/bsd-coherence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.BSD`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.BSD::bsd_coherence_check",
  "declaration_slug": "bsd-coherence-check",
  "kind": "def",
  "name": "bsd_coherence_check",
  "module_name": "TauLib.BookIII.Arithmetic.BSD",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-bsd/",
  "source_line_start": 38,
  "source_line_end": 55,
  "registry_ids": [
    "III.T35"
  ],
  "related_registry_items": [
    {
      "id": "III.T35",
      "title": "BSD Coherence Theorem",
      "url": "/registry/object/III.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L38-L55",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.BSD",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-bsd/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L38-L55",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Arithmetic.BSD](/corpus/taulib/docs/book-iii-arithmetic-bsd/)
- Source path: [`TauLib/BookIII/Arithmetic/BSD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L38-L55)
- Source range: L38-L55
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.T35` — BSD Coherence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T35] BSD coherence: the BSD functional stabilizes across depths.
    BSD_τ(k) at k is compatible with BSD_τ(k+1) at k+1. -/
```

## Source Excerpt

```lean
def bsd_coherence_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let bsd_k := bsd_functional k
      let bsd_k1 := bsd_functional (k + 1)
      -- Coherence: sector products at k divide those at k+1 (tower extension)
      let bp_k := split_zeta_b k
      let bp_k1 := split_zeta_b (k + 1)
      let cp_k := split_zeta_c k
      let cp_k1 := split_zeta_c (k + 1)
      let coherent := (if bp_k > 0 then bp_k1 % bp_k == 0 else true) &&
                      (if cp_k > 0 then cp_k1 % cp_k == 0 else true)
      coherent && go (k + 1) (fuel - 1)
  termination_by fuel
```
