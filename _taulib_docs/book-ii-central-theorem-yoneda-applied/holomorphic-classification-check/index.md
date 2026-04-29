---
{
  "projection_kind": "taulib_declaration",
  "title": "holomorphic_classification_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/holomorphic-classification-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::holomorphic_classification_check",
  "declaration_slug": "holomorphic-classification-check",
  "kind": "def",
  "name": "holomorphic_classification_check",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 173,
  "source_line_end": 198,
  "registry_ids": [
    "II.T39"
  ],
  "related_registry_items": [
    {
      "id": "II.T39",
      "title": "Omega-Germs iff Holomorphic Functions",
      "url": "/registry/object/II.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L173-L198",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L173-L198",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L173-L198)
- Source range: L173-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T39` — Omega-Germs iff Holomorphic Functions

## Immediate Comment / Docstring

```lean
/-- [II.T39] Holomorphic classification check: verify the complete chain
    tower coherence ==> idempotent support ==> bipolar decomposition
    ==> unique omega-germ.

    For each test point x at stage k:
    1. Tower coherence of id_stage gives reduce-compatibility
    2. Idempotent support: interior_bipolar decomposes into e_plus and e_minus
    3. Bipolar decomposition: independent B and C channels
    4. Unique omega-germ: Code extraction is deterministic -/
```

## Source Excerpt

```lean
def holomorphic_classification_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let rx := reduce x k
      -- Step 1: Tower coherence
      let tc_ok := reduce (reduce x (k + 1)) k == rx
      -- Step 2: Idempotent support
      let p := from_tau_idx rx
      let bp := interior_bipolar p
      let fp := SectorPair.mul e_plus_sector bp
      let fm := SectorPair.mul e_minus_sector bp
      let is_ok := SectorPair.add fp fm == bp
      -- Step 3: Bipolar orthogonality
      let orth_ok := SectorPair.mul fp fm == (SectorPair.mk 0 0)
      -- Step 4: Unique omega-germ (Code vs pre-Yoneda agreement)
      let b_fn : TauIdx -> Int := fun n => (reduce n k : Int)
      let code_val := code_extract b_fn k x
      let yoneda_val := (preyoneda_embed_nat (fun n => reduce n k) x k : Int)
      let det_ok := code_val == yoneda_val
      tc_ok && is_ok && orth_ok && det_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
