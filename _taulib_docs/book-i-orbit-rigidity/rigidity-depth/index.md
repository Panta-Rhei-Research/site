---
{
  "projection_kind": "taulib_declaration",
  "title": "rigidity_depth",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/rigidity-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::rigidity_depth",
  "declaration_slug": "rigidity-depth",
  "kind": "theorem",
  "name": "rigidity_depth",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 64,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L64-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Rigidity",
        "url": "/verify/taulib/docs/book-i-orbit-rigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L64-L129",
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

- Module: [TauLib.BookI.Orbit.Rigidity](/verify/taulib/docs/book-i-orbit-rigidity/)
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L64-L129)
- Source range: L64-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- φ maps depth-0 non-omega objects to depth 0. -/
```

## Source Excerpt

```lean
theorem rigidity_depth (φ : TauAutomorphism) (g : Generator) (hg : g ≠ omega) :
    (φ.toFun ⟨g, 0⟩).depth = 0 := by
  -- Find preimage y of ⟨(φ(g,0)).seed, 0⟩
  have hy_img := φ.right_inv ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩
  -- y = φ⁻¹(⟨seed, 0⟩), φ(y) = ⟨seed, 0⟩
  -- y cannot be omega-fiber
  have hy_ne : (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed ≠ omega := by
    intro h_om
    -- φ maps omega objects to omega objects
    have h1 := auto_omega_to_omega φ (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).depth
    -- Rewrite ⟨omega, y.depth⟩ = y (since y.seed = omega)
    have h_eta : (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩) =
        ⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed,
         (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).depth⟩ := by
      cases (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩); rfl
    rw [h_om] at h_eta
    rw [← h_eta] at h1
    -- h1: (φ(y)).seed = omega, but φ(y) = ⟨(φ(g,0)).seed, 0⟩
    rw [hy_img] at h1
    -- h1: (φ(g,0)).seed = omega — contradicts auto_non_omega
    exact auto_non_omega φ g hg h1
  -- Apply shift formula to y's orbit
  have h_shift := auto_shift φ
    (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed
    hy_ne
    (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).depth
  -- Rewrite ⟨y.seed, y.depth⟩ = y
  have h_eta2 : (⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed,
                   (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).depth⟩ : TauObj) =
      φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩ := by
    cases (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩); rfl
  rw [h_eta2] at h_shift
  rw [hy_img] at h_shift
  -- h_shift: ⟨(φ(g,0)).seed, 0⟩ = ⟨(φ(⟨y.seed,0⟩)).seed, (φ(⟨y.seed,0⟩)).depth + y.depth⟩
  -- Extract depth: 0 = (φ(⟨y.seed,0⟩)).depth + y.depth
  have h_dep := congrArg TauObj.depth h_shift
  simp at h_dep
  -- Both summands are 0
  have hy_depth_zero : (φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).depth = 0 := by omega
  -- y.depth = 0, so y = ⟨y.seed, 0⟩, so φ(⟨y.seed, 0⟩) = ⟨seed, 0⟩
  have h_base : φ.toFun ⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed, 0⟩ =
      ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩ := by
    have h_y_eq : φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩ =
        ⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed, 0⟩ := by
      have := h_eta2.symm
      rw [hy_depth_zero] at this
      exact this
    rw [← h_y_eq]; exact hy_img
  -- Now: φ(⟨y.seed, d₀⟩) = ⟨seed, d₀⟩ (from shift + base)
  have h_yd : φ.toFun ⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed, (φ.toFun ⟨g, 0⟩).depth⟩ =
      ⟨(φ.toFun ⟨g, 0⟩).seed, (φ.toFun ⟨g, 0⟩).depth⟩ := by
    have h := auto_shift φ _ hy_ne (φ.toFun ⟨g, 0⟩).depth
    have h_s := congrArg TauObj.seed h_base
    have h_d := congrArg TauObj.depth h_base
    simp at h_s h_d
    rw [h_s, h_d] at h; simpa using h
  -- φ(⟨g, 0⟩) = ⟨seed, d₀⟩ (by eta)
  have h_g : φ.toFun ⟨g, 0⟩ = ⟨(φ.toFun ⟨g, 0⟩).seed, (φ.toFun ⟨g, 0⟩).depth⟩ := by
    cases (φ.toFun ⟨g, 0⟩); rfl
  -- Injectivity gives ⟨g, 0⟩ = ⟨y.seed, d₀⟩
  have h_eq : φ.toFun ⟨g, 0⟩ = φ.toFun ⟨(φ.invFun ⟨(φ.toFun ⟨g, 0⟩).seed, 0⟩).seed,
      (φ.toFun ⟨g, 0⟩).depth⟩ := by
    rw [h_g, h_yd]
  have h_eq2 := congrArg φ.invFun h_eq
  rw [φ.left_inv, φ.left_inv] at h_eq2
  exact (congrArg TauObj.depth h_eq2).symm
```
