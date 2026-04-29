---
{
  "projection_kind": "taulib_declaration",
  "title": "four_gen_order_rigid",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-few/four-gen-order-rigid/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooFew`.",
  "declaration_id": "TauLib.BookI.Orbit.TooFew::four_gen_order_rigid",
  "declaration_slug": "four-gen-order-rigid",
  "kind": "theorem",
  "name": "four_gen_order_rigid",
  "module_name": "TauLib.BookI.Orbit.TooFew",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-few/",
  "source_line_start": 122,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L122-L162",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooFew",
        "url": "/verify/taulib/docs/book-i-orbit-too-few/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L122-L162",
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

- Module: [TauLib.BookI.Orbit.TooFew](/verify/taulib/docs/book-i-orbit-too-few/)
- Source path: [`TauLib/BookI/Orbit/TooFew.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L122-L162)
- Source range: L122-L162
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The only permutations of Gen4 fixing α and ω are
    id and the transposition (π γ). The transposition reverses
    the canonical order (π < γ becomes γ > π), so an order-preserving
    bijection must be the identity. -/
```

## Source Excerpt

```lean
theorem four_gen_order_rigid (f : Gen4 → Gen4)
    (hf_alpha : f alpha = alpha)
    (hf_omega : f omega = omega)
    (hf_order : ∀ g h : Gen4, Gen4.toNat g < Gen4.toNat h →
                             Gen4.toNat (f g) < Gen4.toNat (f h)) :
    ∀ g, f g = g := by
  -- Key: order-preservation + fixed endpoints force f pi = pi and f gamma = gamma.
  -- From alpha < pi < gamma < omega and f(alpha)=alpha, f(omega)=omega:
  --   0 < toNat(f pi) < toNat(f gamma) < 3
  -- So toNat(f pi) ∈ {1,2} and toNat(f gamma) ∈ {1,2} with strict inequality.
  -- The only solution is toNat(f pi) = 1, toNat(f gamma) = 2.
  have h_ap := hf_order alpha pi (by decide)
  have h_pg := hf_order pi gamma (by decide)
  have h_go := hf_order gamma omega (by decide)
  rw [hf_alpha] at h_ap
  rw [hf_omega] at h_go
  -- h_ap: 0 < toNat (f pi)
  -- h_pg: toNat (f pi) < toNat (f gamma)
  -- h_go: toNat (f gamma) < 3
  -- Chain: 0 < toNat(f pi) < toNat(f gamma) < 3
  -- Only solution: toNat(f pi) = 1 ∧ toNat(f gamma) = 2
  -- Recover f pi = pi from toNat constraints
  have hfp : f pi = pi := by
    cases hc : f pi with
    | alpha => rw [hc] at h_ap; simp [Gen4.toNat] at h_ap
    | pi => rfl
    | gamma => rw [hc] at h_pg; simp [Gen4.toNat] at h_pg h_go; omega
    | omega => rw [hc] at h_pg; simp [Gen4.toNat] at h_pg h_go; omega
  -- Recover f gamma = gamma from toNat constraints
  have hfg : f gamma = gamma := by
    cases hc : f gamma with
    | alpha => rw [hfp, hc] at h_pg; simp [Gen4.toNat] at h_pg
    | pi => rw [hfp, hc] at h_pg; simp [Gen4.toNat] at h_pg
    | gamma => rfl
    | omega => rw [hc] at h_go; simp [Gen4.toNat] at h_go
  intro g
  cases g with
  | alpha => exact hf_alpha
  | omega => exact hf_omega
  | pi => exact hfp
  | gamma => exact hfg
```
